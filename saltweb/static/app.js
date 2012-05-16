function MinionCtrl($scope, $http){
  $scope.minions = [];
  $scope.keys_all = '';
  $scope.keys_acc = '';
  $scope.keys_pre = '';
  $scope.keys_rej = '';

  $scope.get_all = function(){
      get_minions($scope, $http, 'http://0.0.0.0:6543/keys/list/all/');
      clear_active($scope);
      $scope.keys_all = 'active';
  };
  $scope.get_pre = function(){
      get_minions($scope, $http, 'http://0.0.0.0:6543/keys/list/pre/');
      clear_active($scope);
      $scope.keys_pre = 'active';
  };
  $scope.get_rej = function(){
      get_minions($scope, $http, 'http://0.0.0.0:6543/keys/list/rej/');
      clear_active($scope);
      $scope.keys_rej = 'active';
  };
  $scope.get_acc = function(){
      get_minions($scope, $http, 'http://0.0.0.0:6543/keys/list/acc/');
      clear_active($scope);
      $scope.keys_acc = 'active';
  };
  $scope.get_all();
}

function clear_active($scope){
    $scope.keys_all = '';
    $scope.keys_acc = '';
    $scope.keys_pre = '';
    $scope.keys_rej = '';
}

function get_minions($scope, $http, url){
    $http.get(url).
      success(function(data){
        $scope.minions = data;
      });
}
