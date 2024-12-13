import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonButton,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonImg,
  IonSelect,
  IonSelectOption,
} from '@ionic/angular/standalone';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonButton,
    IonImg,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonSelect,
    IonSelectOption,
    FormsModule,
    CommonModule,
  ],
})
export class HomePage {
  public image: File | undefined;
  public imageSrc: string = '';
  public convertedImg: string = '';
  public filter: string = 'origin';
  constructor() {}

  async getImage(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const fileReader = new FileReader();
      fileReader.onload = () => {
        if (typeof fileReader.result == 'string')
          this.imageSrc = fileReader.result;
      };
      fileReader.readAsDataURL(input.files[0]);
      this.image = input.files[0];
    }
  }
  async uploadTest() {
    if (!this.image) {
      alert('no image!');
      return;
    }
    console.log(this.image);

    const formData = new FormData();
    formData.append('image', this.image);
    formData.append('filter', this.filter);

    try {
      const response = await fetch('http://localhost:4000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('failed');
      }
      const result = await response.blob();
      const url = URL.createObjectURL(result);
      this.convertedImg = url;
      console.log(url);
    } catch (e) {
      console.log(JSON.stringify(e));
    }
  }
}
