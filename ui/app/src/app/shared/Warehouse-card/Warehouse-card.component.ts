import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Warehouse-card.component.html',
  styleUrls: ['./Warehouse-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Warehouse-card]': 'true'
  }
})

export class WarehouseCardComponent {


}