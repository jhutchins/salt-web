import salt
from salt.cli.key import Key

__all__ = ['KeyManager', 'get_acc', 'get_all', 'get_pre', 'get_rej']

#Setup the KeyManager
opts = salt.config.master_config('/etc/salt/master')
opts.update({'quiet': False})
Labels = {
    'pre': {
        'status': 'unaccepted',
        'label': 'important'
    },
    'acc': {
        'status': 'accepted',
        'label': 'success',
    },
    'rej': {
        'status': 'rejected',
        'label': 'info',
    },
}

KeyManager = Key(opts)

def _get_keys(key_type):
    ret = []
    for key in KeyManager._keys(key_type):
        obj = {'name': key}
        obj.update(Labels[key_type])
        ret.append(obj)
    ret.sort(cmp=lambda x, y: cmp(x['name'], y['name']))
    return ret

def get_acc():
    return _get_keys('acc')

def get_all():
    ret = []
    ret += get_pre()
    ret += get_rej()
    ret += get_acc()
    ret.sort(cmp=lambda x, y: cmp(x['name'], y['name']))
    return ret

def get_pre():
    return _get_keys('pre')

def get_rej():
    return _get_keys('rej')
