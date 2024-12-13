import { Component } from '@angular/core';
import { Router } from '@angular/router';
import {
  IonApp,
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonItem,
  IonList,
  IonMenu,
  IonMenuButton,
  IonRouterOutlet,
  IonSplitPane,
  IonTitle,
  IonToolbar,
} from '@ionic/angular/standalone';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  standalone: true,
  imports: [
    IonApp,
    IonRouterOutlet,
    IonSplitPane,
    IonMenu,
    IonHeader,
    IonToolbar,
    IonList,
    IonItem,
    IonButton,
    IonTitle,
    IonContent,
    IonButtons,
    IonMenuButton,
  ],
})
export class AppComponent {
  constructor(private router: Router) {}

  go(url: string) {
    this.router.navigate([url]);
  }
}
