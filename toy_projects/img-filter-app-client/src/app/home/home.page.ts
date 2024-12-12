import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
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
    FormsModule,
    CommonModule,
  ],
})
export class HomePage {
  public image: File | undefined;
  public convertedImg: Array<{ src: string; title: string }> = [];
  constructor() {}

  async getImage(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
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
      this.convertedImg.push({ src: url, title: 'test' });
      console.log(url);
    } catch (e) {
      console.log(JSON.stringify(e));
    }
  }
}
