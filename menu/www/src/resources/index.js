'use strict';

import MenuResource from './menuResource';
import MenuDishResource from './menuDishResource'


let module = angular.module('app.resources', [])
    .factory('MenuResource', MenuResource)
    .factory('MenuDishResource', MenuDishResource);

export default module.name;
