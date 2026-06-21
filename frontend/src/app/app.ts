import { HttpClient } from '@angular/common/http';
import { Component, computed, inject, OnInit, signal } from '@angular/core';

interface UploadResponse {
  message: string;
  resume_id: number;
}

interface DomainOption {
  id: string;
  label: string;
  description: string;
  icon: string;
}

interface SkillItem {
  key: string;
  label: string;
  matched: boolean;
}

interface CategoryGroup {
  category: string;
  skills: SkillItem[];
}

interface Recommendation {
  title: string;
  detail: string;
  priority: 'high' | 'medium' | 'low';
  category?: string;
}

interface DomainCandidate {
  domain: string;
  label: string;
  matches: number;
  ratio: number;
}

interface CrossDomainSkill {
  key: string;
  label: string;
  domain: string;
  domain_label: string;
}

interface AnalysisResponse {
  resume_id: number;
  filename: string;
  domain: string;
  domain_label: string;
  auto_detected: boolean;
  domain_candidates: DomainCandidate[];
  score: number;
  grade: string;
  summary: string;
  found_skills: string[];
  missing_skills: string[];
  found_count: number;
  missing_count: number;
  total_skills: number;
  match_percentage: string;
  categories: CategoryGroup[];
  cross_domain_skills: CrossDomainSkill[];
  recommendations: Recommendation[];
  is_new_analysis: boolean;
}

type Step = 'idle' | 'uploading' | 'analyzing' | 'done';

@Component({
  selector: 'app-root',
  imports: [],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App implements OnInit {
  private readonly http = inject(HttpClient);
  private readonly apiBase = 'http://127.0.0.1:8000/api';

  protected readonly domains = signal<DomainOption[]>([]);
  protected readonly selectedDomain = signal('auto');
  protected readonly selectedFile = signal<File | null>(null);
  protected readonly dragOver = signal(false);
  protected readonly step = signal<Step>('idle');
  protected readonly errorMessage = signal('');
  protected readonly analysis = signal<AnalysisResponse | null>(null);

  protected readonly loading = computed(() => {
    const step = this.step();
    return step === 'uploading' || step === 'analyzing';
  });

  protected readonly scoreRingStyle = computed(() => {
    const score = this.analysis()?.score ?? 0;
    const color = score >= 70 ? '#22d3ee' : score >= 40 ? '#fbbf24' : '#f87171';
    return {
      background: `conic-gradient(${color} ${score * 3.6}deg, rgba(255,255,255,0.08) 0deg)`,
    };
  });

  protected readonly selectableDomains = computed(() =>
    this.domains().filter((d) => d.id !== 'auto'),
  );

  ngOnInit(): void {
    this.http.get<{ domains: DomainOption[] }>(`${this.apiBase}/domains/`).subscribe({
      next: (res) => this.domains.set(res.domains),
      error: () => {
        this.domains.set([{
          id: 'auto',
          label: 'Auto-detect field',
          description: 'Automatically identify your major from CV content',
          icon: 'sparkles',
        }]);
      },
    });
  }

  selectDomain(domainId: string): void {
    this.selectedDomain.set(domainId);
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.setFile(input.files?.[0] ?? null);
  }

  onDrop(event: DragEvent): void {
    event.preventDefault();
    this.dragOver.set(false);
    const file = event.dataTransfer?.files?.[0] ?? null;
    this.setFile(file);
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault();
    this.dragOver.set(true);
  }

  onDragLeave(): void {
    this.dragOver.set(false);
  }

  analyzeCv(): void {
    const file = this.selectedFile();
    if (!file) {
      return;
    }

    this.step.set('uploading');
    this.errorMessage.set('');
    this.analysis.set(null);

    const formData = new FormData();
    formData.append('file', file);

    this.http.post<UploadResponse>(`${this.apiBase}/upload/`, formData).subscribe({
      next: (upload) => {
        this.step.set('analyzing');
        this.http
          .post<AnalysisResponse>(`${this.apiBase}/analyze/${upload.resume_id}/`, {
            domain: this.selectedDomain(),
          })
          .subscribe({
            next: (result) => {
              this.analysis.set(result);
              this.step.set('done');
            },
            error: (error) => {
              this.errorMessage.set(this.extractError(error));
              this.step.set('idle');
            },
          });
      },
      error: (error) => {
        this.errorMessage.set(this.extractError(error));
        this.step.set('idle');
      },
    });
  }

  reset(): void {
    this.selectedFile.set(null);
    this.selectedDomain.set('auto');
    this.step.set('idle');
    this.errorMessage.set('');
    this.analysis.set(null);
  }

  formatSize(bytes: number): string {
    if (bytes < 1024) {
      return `${bytes} B`;
    }
    if (bytes < 1024 * 1024) {
      return `${(bytes / 1024).toFixed(1)} KB`;
    }
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  }

  priorityLabel(priority: Recommendation['priority']): string {
    if (priority === 'high') {
      return 'High impact';
    }
    if (priority === 'medium') {
      return 'Recommended';
    }
    return 'Insight';
  }

  private setFile(file: File | null): void {
    if (!file) {
      this.selectedFile.set(null);
      return;
    }

    if (!file.name.toLowerCase().endsWith('.pdf')) {
      this.errorMessage.set('Please upload a PDF file.');
      return;
    }

    this.selectedFile.set(file);
    this.errorMessage.set('');
    this.analysis.set(null);
    this.step.set('idle');
  }

  private extractError(error: { error?: { error?: string }; message?: string }): string {
    return error.error?.error ?? error.message ?? 'Something went wrong. Please try again.';
  }
}
