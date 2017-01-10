import MenuModalComponent from './menuModal.component';

import './menuModal.sass'

let module = angular.module('app.menu', [])
    .component('menuModal', MenuModalComponent);

export default module.name;