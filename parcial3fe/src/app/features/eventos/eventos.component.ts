import { Component, OnInit } from '@angular/core';
import { PruebaService } from '../../services/prueba.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ActivatedRoute, Route, Router } from '@angular/router';

@Component({
  selector: 'app-eventos',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './eventos.component.html',
  styleUrl: './eventos.component.css',
  providers: [PruebaService],
})
export class EventosComponent implements OnInit {

  constructor(
    private pruebaService: PruebaService,
    private route: ActivatedRoute,
    private router: Router
  ) {}
  eventos: any;
  direccion: any;
  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.direccion = params['direccion'];
      this.pruebaService.buscarPorLongLat(this.direccion).subscribe((data) => {

        this.eventos = data
      });
    });
    
  }

  onClickGoToDetails(eventoId : string) {
    this.router.navigate(['detalles',eventoId]);
  }
}
