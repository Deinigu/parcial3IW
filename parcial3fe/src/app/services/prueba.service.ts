import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Prueba } from '../interfaces/prueba';

@Injectable({
  providedIn: 'root',
})
export class PruebaService {
  constructor(private http: HttpClient) {}

  getAllPruebas(): Observable<any> {
    const url = 'http://13.38.223.212:8000/api/prueba/';
    return this.http.get<any>(url);
  }

  getPruebaInfo(idPrueba: string): Observable<any> {
    const url = 'http://13.38.223.212:8000/api/prueba/' + idPrueba + '/';
    return this.http.get<any>(url);
  }

  createPrueba(prueba: Prueba): Observable<any> {
    const url = 'http://13.38.223.212:8000/api/prueba/';
    return this.http.post<any>(url, prueba);
  }

  editPrueba(idPrueba: string, prueba: Prueba): Observable<any> {
    const url = 'http://13.38.223.212:8000/api/prueba/' + idPrueba + '/';
    return this.http.put<any>(url, prueba);
  }

  deletePrueba(idPrueba: string): Observable<any> {
    const url = 'http://13.38.223.212:8000/api/prueba/' + idPrueba + '/';
    return this.http.delete<any>(url);
  }

  buscarPorLongLat(direccion : string): Observable<any>{
    const url = 'http://13.38.223.212:8000/api/prueba/busquedaLatLot/' + direccion + '/';
    return this.http.get<any>(url);
  }

}
