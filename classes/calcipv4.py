import re


class CalcIPv4:
    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        self._set_broadcast()
        self._set_net()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @property
    def net(self):
        return self._net

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def num_of_ips(self):
        return self._get_num_of_ips()

    @ip.setter
    def ip(self, ip_num):
        if not self._ip_validation(ip_num):
            raise ValueError("Invalid IP.")
        self._ip = ip_num
        self._ip_bin = self._ip_to_bin(ip_num)

    @mask.setter
    def mask(self, mask_num):
        if not mask_num:
            return
        if not self._ip_validation(mask_num):
            raise ValueError("Invalid Mask.")
        self._mask = mask_num
        self._mask_bin = self._ip_to_bin(mask_num)

        if not hasattr(self, 'prefix'):
            self._prefix = self._mask_bin.count('1')

    @prefix.setter
    def prefix(self, prefix_num):
        if not prefix_num:
            return
        if not isinstance(prefix_num, int):
            raise TypeError('Prefix needs to be an integer.')
        if prefix_num > 32:
            raise TypeError('Prefix needs to be lower than 32 Bits.')
        self._prefix = prefix_num
        self._mask_bin = (prefix_num * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self._mask = self._bin_to_ip(self._mask_bin)

    @staticmethod
    def _ip_validation(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocks = ip.split('.')
        bin_blocks = [bin(int(x))[2:].zfill(8) for x in blocks]
        return ''.join(bin_blocks)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocks = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocks)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[:self.prefix] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_net(self):
        host_bits = 32 - self.prefix
        self._net_bin = self._ip_bin[:self.prefix] + (host_bits * '0')
        self._net = self._bin_to_ip(self._net_bin)
        return self._net

    def _get_num_of_ips(self):
        return 2 ** (32 - self.prefix)
