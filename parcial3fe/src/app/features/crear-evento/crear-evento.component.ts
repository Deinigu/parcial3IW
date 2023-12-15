import { Component } from '@angular/core';
import { ImagenService } from '../../services/imagen.service';
import { PruebaService } from '../../services/prueba.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Prueba } from '../../interfaces/prueba';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-crear-evento',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './crear-evento.component.html',
  styleUrl: './crear-evento.component.css',
  providers: [ImagenService, PruebaService],
})
export class CrearEventoComponent {
  selectedFiles: File[] = [];
  urls: any[] = [];
  fotos_subidas: boolean = false;
  prueba: Prueba = {
    nombre: '',
    timestamp: new Date(),
    lugar: '',
    lat: 0,
    lon: 0,
    organizador: '',
    imagen: '',
  };

  evento_subido : boolean = false;

  constructor(
    private http: HttpClient,
    private imagenService: ImagenService,
    private router: Router,
    private pruebaService: PruebaService
  ) {}
  ngOnInit(): void {
    this.fotos_subidas = false;
    this.evento_subido = false;
  }

  // Cloudinary
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      this.selectedFiles = Array.from(input.files);
    }
  }

  onButtonClicked(): void {
    if (this.selectedFiles.length > 0) {
      this.imagenService
        .uploadImage(this.selectedFiles)
        .subscribe((response) => {
          if (response) {
            this.urls = response.urls;
            this.prueba.imagen = this.urls[0];
            console.log(this.prueba.imagen);
            this.fotos_subidas = true;
          }
        });
    }
  }

  onSubmit() {
    let organizador : any;
    organizador = localStorage.getItem('email');
    this.prueba.organizador = organizador;

    this.pruebaService.createPrueba(this.prueba).subscribe(response => {
      console.log(response);
      this.evento_subido = true;
    });
    }
}
