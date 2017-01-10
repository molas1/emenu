import template from './app.html'


const controller = function (MenuResource) {
    this.$onInit = function () {
        this.current_page = 1;
        this.ordering = 'dish_count';
        this.orderingDirection = '';
        this.orderingChoices = [{value: 'pk', label: 'Id'}, {value: 'name', label: 'Name'}, {value: 'dish_count', label: 'Dish count'}];
        this.refreshMenus();
    };

    this.pageChange = (p) => {
        this.current_page = p;
        this.refreshMenus();
    };

    this.changeOrdering = (ordering) => {
        this.ordering = ordering;
    };

    this.flipOrderingDirection = () => {
        if (this.orderingDirection == '') {
            this.orderingDirection = '-';
        }
        else {
            this.orderingDirection = '';
        }
        this.refreshMenus();
    };

    this.refreshMenus = () => {
        this.menus = MenuResource.query({page: this.current_page, ordering: this.orderingDirection + this.ordering});
        this.menus.$promise
            .then(() => {
                this.loaded = true;
            })
            .catch((resp) => {
                console.log(resp);
            });
    };
};

export default {
    template,
    controller: controller,
    controllerAs: 'ctrl'
};