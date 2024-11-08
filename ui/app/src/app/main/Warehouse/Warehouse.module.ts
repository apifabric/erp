import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WAREHOUSE_MODULE_DECLARATIONS, WarehouseRoutingModule} from  './Warehouse-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WarehouseRoutingModule
  ],
  declarations: WAREHOUSE_MODULE_DECLARATIONS,
  exports: WAREHOUSE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WarehouseModule { }