import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'filter',
    loadComponent: () =>
      import('./filter/filter.page').then((m) => m.FilterPage),
  },
  {
    path: '',
    redirectTo: 'filter',
    pathMatch: 'full',
  },
  {
    path: 'mosaic',
    loadComponent: () => import('./mosaic/mosaic.page').then( m => m.MosaicPage)
  },
  {
    path: 'trace-object',
    loadComponent: () => import('./trace-object/trace-object.page').then( m => m.TraceObjectPage)
  },
];
