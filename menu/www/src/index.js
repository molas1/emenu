import 'angular';
import ngRoute from 'angular-route';
import ngResource from 'angular-resource';

import app from './app';
import resources from './resources';

const bootstrap = angular.module('emenus', [app, ngRoute, ngResource, resources]);

bootstrap.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

export default bootstrap;