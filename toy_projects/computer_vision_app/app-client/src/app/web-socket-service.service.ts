import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Injectable({
  providedIn: 'root',
})
export class WebSocketServiceService {
  constructor(private socket: Socket) {}

  sendFrame(frame: string) {
    this.socket.emit('send_frame', { frame });
  }

  getProcessedFrame() {
    debugger;
    return this.socket.fromEvent<{ frame: string }>('receive_frame');
  }
}
