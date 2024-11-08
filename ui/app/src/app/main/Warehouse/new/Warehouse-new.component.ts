import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Warehouse-new',
  templateUrl: './Warehouse-new.component.html',
  styleUrls: ['./Warehouse-new.component.scss']
})
export class WarehouseNewComponent {
  @ViewChild("WarehouseForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}