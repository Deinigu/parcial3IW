import { Routes } from '@angular/router';
import { ImagenesComponent } from './features/imagenes/imagenes.component';
import { InicioComponent } from './features/inicio/inicio.component';
import { OauthComponent } from './features/oauth/oauth.component';
import { MapComponent } from './features/map/map.component';
import { EventosComponent } from './features/eventos/eventos.component';
import { DetallesComponent } from './features/detalles/detalles.component';
import { CrearEventoComponent } from './features/crear-evento/crear-evento.component';

export const routes: Routes = [
    {
        path : '',
        component: InicioComponent,
        title : 'Inicio'
    },
    {
        path : 'eventos/:direccion',
        component: EventosComponent,
        title: 'Eventos'
    },
    {
        path: 'detalles/:id',
        component: DetallesComponent,
        title: 'Detalles'
    },
    {
        path: 'crearEvento',
        component: CrearEventoComponent,
        title: 'Crear Evento'
    }
];
