import { MenuRootItem } from 'ontimize-web-ngx';

import { CategoryCardComponent } from './Category-card/Category-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProductCategoryCardComponent } from './ProductCategory-card/ProductCategory-card.component';

import { ShipmentCardComponent } from './Shipment-card/Shipment-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplierProductCardComponent } from './SupplierProduct-card/SupplierProduct-card.component';

import { WarehouseCardComponent } from './Warehouse-card/Warehouse-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Category', name: 'CATEGORY', icon: 'view_list', route: '/main/Category' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'ProductCategory', name: 'PRODUCTCATEGORY', icon: 'view_list', route: '/main/ProductCategory' }
    
        ,{ id: 'Shipment', name: 'SHIPMENT', icon: 'view_list', route: '/main/Shipment' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplierProduct', name: 'SUPPLIERPRODUCT', icon: 'view_list', route: '/main/SupplierProduct' }
    
        ,{ id: 'Warehouse', name: 'WAREHOUSE', icon: 'view_list', route: '/main/Warehouse' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CategoryCardComponent

    ,CustomerCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PaymentCardComponent

    ,ProductCardComponent

    ,ProductCategoryCardComponent

    ,ShipmentCardComponent

    ,SupplierCardComponent

    ,SupplierProductCardComponent

    ,WarehouseCardComponent

];