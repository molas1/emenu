'use strict';

const MenuResource = function($resource) {
    return $resource('/ng-api/menu/',{},{
      query:{ method:'GET', params:{}, headers:{'Content-Type':'application/json'}}});
};

export default MenuResource;