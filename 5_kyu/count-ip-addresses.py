# DESCRIPTION
# Implement a function that receives two IPv4 addresses, and returns the
# number of addresses between them (including the first one, excluding
# the last one).
#
# All inputs will be valid IPv4 addresses in the form of strings.
# The last address will always be greater than the first one.
#
# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50
# * With input "10.0.0.0", "10.0.1.0"   => return  256
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start: str, end: str) -> int:
    octet_len = 8

    start_as_octets = [format(int(octet), 'b').zfill(octet_len) for octet in start.split('.')]  # noqa
    end_as_octets = [format(int(octet), 'b').zfill(octet_len) for octet in end.split('.')]  # noqa

    start_as_bin = ''.join(start_as_octets)
    end_as_bin = ''.join(end_as_octets)

    return int(end_as_bin, 2) - int(start_as_bin, 2)


if __name__ == '__main__':
    print(ips_between('20.0.0.10', '20.0.1.0'))
    print(ips_between('10.0.0.0', '10.0.0.50'))
    print(ips_between('10.0.0.0', '10.0.1.0'))
