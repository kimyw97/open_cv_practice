import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TraceObjectPage } from './trace-object.page';

describe('TraceObjectPage', () => {
  let component: TraceObjectPage;
  let fixture: ComponentFixture<TraceObjectPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(TraceObjectPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
