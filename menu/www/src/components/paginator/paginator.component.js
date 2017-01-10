import template from './paginator.html'


export default {
    template,
    controller: function () {

        this.$onInit = function () {
            this.page = 1;
            this.count = this.menus.count;
            this.pageSize = 10;
            this.end = Math.floor(this.count / this.pageSize) + (1 ? (this.count % this.pageSize !== 0) : 0);
        };

        this.getIndexes = () => {
            let indexes = [];
            let start = Math.floor((this.page - 1) / this.pageSize) * 10;
            for (let i = start; i <= start + 1 + this.pageSize && i <= this.end; i++) {
                if (i != 0) {
                    indexes.push(i);
                }
            }
            return indexes;
        };

        this.propagate = () => {
            if (typeof this.changeCallback === 'function') {
                this.changeCallback({page: this.page});
            }
        };

        this.nextPage = () => {
            if (this.page < this.end) {
                this.page = this.page + 1;
                this.propagate();
            }
        };

        this.previousPage = () => {
            if (this.page > 1) {
                this.page = this.page - 1;
                this.propagate();
            }
        };

        this.changePage = (p) => {
            this.page = p;
            this.propagate();
        }
    },
    controllerAs: 'ctrl',
    bindings: {
        menus: '<',
        changeCallback: '&pageSwitch'
    }
};