import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PruebaService } from '../../services/prueba.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-inicio',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './inicio.component.html',
  styleUrl: './inicio.component.css',
  providers: [PruebaService]
})
export class InicioComponent implements OnInit{
  constructor(private router: Router){

  }
  name : any;
  ngOnInit(): void {
    this.name = localStorage.getItem("name");
  }

  redirectBusqueda(busqueda: { busca : string }){
    const direccion = busqueda.busca;
    if(direccion == '')
    {
      this.router.navigate(['/']);
    }
    else {
      this.router.navigate(['/eventos/' + direccion]);
    }
  }


}
