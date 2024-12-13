import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  IonButtons,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonContent,
  IonHeader,
  IonMenuButton,
  IonRadio,
  IonRadioGroup,
  IonTitle,
  IonToolbar,
} from '@ionic/angular/standalone';

@Component({
  selector: 'app-mosaic',
  templateUrl: './mosaic.page.html',
  styleUrls: ['./mosaic.page.scss'],
  standalone: true,
  imports: [
    IonContent,
    IonHeader,
    IonTitle,
    IonToolbar,
    CommonModule,
    FormsModule,
    IonButtons,
    IonMenuButton,
    IonRadio,
    IonRadioGroup,
    IonCard,
    IonCardContent,
    IonCardHeader,
  ],
})
export class MosaicPage implements OnInit {
  public method: string = 'resize';
  public convertedImg: string = '';
  constructor() {}

  ngOnInit() {}

  async imageUpload(e: Event) {
    const input = e.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const formData = new FormData();
      formData.append('image', input.files[0]);
      formData.append('mosaicMethod', this.method);

      try {
        const response = await fetch('http://localhost:4000/mosaic', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('failed');
        }
        const result = await response.blob();
        const url = URL.createObjectURL(result);
        this.convertedImg = url;
      } catch (e) {
        console.log(e);
      }
    }
  }
}
