import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WarehouseHomeComponent } from './home/Warehouse-home.component';
import { WarehouseNewComponent } from './new/Warehouse-new.component';
import { WarehouseDetailComponent } from './detail/Warehouse-detail.component';

const routes: Routes = [
  {path: '', component: WarehouseHomeComponent},
  { path: 'new', component: WarehouseNewComponent },
  { path: ':id', component: WarehouseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Warehouse-detail-permissions'
      }
    }
  },{
    path: ':warehouse_id/Shipment', loadChildren: () => import('../Shipment/Shipment.module').then(m => m.ShipmentModule),
    data: {
        oPermission: {
            permissionId: 'Shipment-detail-permissions'
        }
    }
}
];

export const WAREHOUSE_MODULE_DECLARATIONS = [
    WarehouseHomeComponent,
    WarehouseNewComponent,
    WarehouseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WarehouseRoutingModule { }