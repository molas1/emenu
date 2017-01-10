import template from './menus.html'

export default {
    template,
    controller: function (MenuDishResource, $timeout) {

        this.$onInit = function () {
            this.selected = null;
        };

        this.menuItemClicked = function (menuId) {
            this.selected = menuId;
            this.dishes = MenuDishResource.query({id: menuId}).$promise
                .then((result) => {
                    this.loaded = true;
                    this.loadeddishes = result;
                })
                .catch((resp) => {
                    console.log(resp);
                });
        };

        this.onMenuModalClose = () => {
            this.selected = null;
            this.loaded = false;
        };
    },
    controllerAs: 'ctrl',
    bindings: {
        menus: '<',
    }
};