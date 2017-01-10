import menus from '../components/menus';
import paginator from '../components/paginator'

import AppComponent from './app.component';

import './app.sass'

const module = angular.module('app', [menus, paginator])
    .component('app', AppComponent);

export default module.name