import { Component } from '@angular/core';
import { PruebaService } from '../../services/prueba.service';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-detalles',
  standalone: true,
  imports: [],
  templateUrl: './detalles.component.html',
  styleUrl: './detalles.component.css',
  providers : [PruebaService, DatePipe]
})
export class DetallesComponent {
  constructor(
    private pruebaService: PruebaService,
    private route: ActivatedRoute,
    private router: Router,
    private datePipe: DatePipe
  ) {}

  idEvento: any;
  evento: any;

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.idEvento = params['id'];
      this.pruebaService.getPruebaInfo(this.idEvento).subscribe((data) => {
        this.evento = data;
        this.evento.fecha = this.datePipe.transform(this.evento.fecha, 'yyyy-MM-dd'); 
      });
    });
  }
}
