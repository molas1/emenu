import template from './menuModal.html'

export default {
    template,
    controller: function (MenuDishResource) {
        this.$onInit = function () {
        };

        this.close = () => {
            this.closeCallback();
        };
    },
    controllerAs: 'ctrl',
    bindings: {
        dishes: '=',
        closeCallback: '&onClose'
    }
};