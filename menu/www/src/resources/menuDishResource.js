'use strict';

const MenuDishResource = function($resource) {
    return $resource('/ng-api/menu/:id/', {},
        {query:{ method:'GET', isArray: false}});
};

export default MenuDishResource;
