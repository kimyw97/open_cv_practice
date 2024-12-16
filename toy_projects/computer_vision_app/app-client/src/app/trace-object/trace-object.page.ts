import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  IonCardContent,
  IonContent,
  IonHeader,
  IonTitle,
  IonCard,
  IonToolbar,
  IonCardHeader,
  IonButton,
} from '@ionic/angular/standalone';
import { WebSocketServiceService } from '../web-socket-service.service';

@Component({
  selector: 'app-trace-object',
  templateUrl: './trace-object.page.html',
  styleUrls: ['./trace-object.page.scss'],
  standalone: true,
  imports: [
    IonContent,
    IonHeader,
    IonTitle,
    IonToolbar,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonButton,
    CommonModule,
    FormsModule,
  ],
})
export class TraceObjectPage implements OnInit {
  public processedFrame: string = '';
  private isRecoding: boolean = false;
  @ViewChild('video') video!: ElementRef<HTMLVideoElement>;
  @ViewChild('canvas') canvas!: ElementRef<HTMLCanvasElement>;
  constructor(private webSocketService: WebSocketServiceService) {}

  ngOnInit() {
    this.webSocketService.getProcessedFrame().subscribe((data) => {
      console.log(data);
      this.processedFrame = `data:image/jpeg;base64,${data.frame}`;
    });
    setInterval(() => this.captureAndSendFrame(), 100);
  }

  startWebCam() {
    this.isRecoding = true;
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
      this.video.nativeElement.srcObject = stream;
    });
  }

  captureAndSendFrame() {
    if (!this.isRecoding) return;
    const video = this.video.nativeElement;
    const canvas = this.canvas.nativeElement;
    const ctx = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    ctx?.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob((blob) => {
      if (blob) {
        const reader = new FileReader();
        reader.onload = () => {
          const base64Data = reader.result?.toString().split(',')[1];
          if (base64Data) {
            this.webSocketService.sendFrame(base64Data);
          }
        };
        reader.readAsDataURL(blob);
      }
    });
  }
}
