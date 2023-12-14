import { Routes } from '@angular/router';
import { ImagenesComponent } from './features/imagenes/imagenes.component';
import { InicioComponent } from './features/inicio/inicio.component';
import { OauthComponent } from './features/oauth/oauth.component';

export const routes: Routes = [
    {
        path : '',
        component: InicioComponent,
        title : 'Inicio'
    },
    {
        path : 'imagen',
        component : ImagenesComponent,
        title : 'Prueba imagen'
    },
    {
        path : 'oauth',
        component: OauthComponent,
        title: 'Oauth'
    }
];
