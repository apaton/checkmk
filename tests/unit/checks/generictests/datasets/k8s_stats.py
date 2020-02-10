# -*- encoding: utf-8
# yapf: disable
checkname = 'k8s_stats'

info = [
    [
        u'{"network": {"tx_dropped": 0, "rx_packets": 138579713, "name": "eth0eth0eth0", "rx_bytes": 255668578132, "tx_errors": 0, "interfaces": [{"tx_dropped": 0, "rx_packets": 27938601, "name": "eth0", "rx_bytes": 66270703699, "tx_errors": 0, "tx_bytes": 6741313890, "rx_dropped": 0, "tx_packets": 24730953, "rx_errors": 0}, {"tx_dropped": 0, "rx_packets": 19431812, "name": "cbr0", "rx_bytes": 3937726843, "tx_errors": 0, "tx_bytes": 60270654692, "rx_dropped": 0, "tx_packets": 22147430, "rx_errors": 0}, {"tx_dropped": 0, "rx_packets": 41698636, "name": "eth0", "rx_bytes": 111016504455, "tx_errors": 0, "tx_bytes": 9524184437, "rx_dropped": 0, "tx_packets": 37783999, "rx_errors": 0}, {"tx_dropped": 0, "rx_packets": 32033132, "name": "cbr0", "rx_bytes": 5574866151, "tx_errors": 0, "tx_bytes": 102989209987, "rx_dropped": 0, "tx_packets": 36262872, "rx_errors": 0}, {"tx_dropped": 0, "rx_packets": 68942476, "name": "eth0", "rx_bytes": 78381369978, "tx_errors": 0, "tx_bytes": 14358691723, "rx_dropped": 0, "tx_packets": 65014942, "rx_errors": 0}, {"tx_dropped": 0, "rx_packets": 57242186, "name": "cbr0", "rx_bytes": 6657123557, "tx_errors": 0, "tx_bytes": 59168669231, "rx_dropped": 0, "tx_packets": 59614737, "rx_errors": 0}], "udp": {"RxQueued": 0, "Listen": 0, "Dropped": 0, "TxQueued": 0}, "tcp": {"Established": 0, "FinWait2": 0, "TimeWait": 0, "FinWait1": 0, "LastAck": 0, "CloseWait": 0, "Close": 0, "Closing": 0, "SynSent": 0, "SynRecv": 0, "Listen": 0}, "udp6": {"RxQueued": 0, "Listen": 0, "Dropped": 0, "TxQueued": 0}, "tcp6": {"Established": 0, "FinWait2": 0, "TimeWait": 0, "FinWait1": 0, "LastAck": 0, "CloseWait": 0, "Close": 0, "Closing": 0, "SynSent": 0, "SynRecv": 0, "Listen": 0}, "tx_bytes": 30624190050, "rx_dropped": 0, "tx_packets": 127529894, "rx_errors": 0}, "timestamp": 1550235205.3, "filesystem": [{"available": 6338084864, "capacity": 10340831232, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 1192403, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 1280000, "device": "shm", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 3985969152, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 53166080, "capacity": 60985344, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 72213, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 74444, "device": "tmpfs", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 7819264, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 6338084864, "capacity": 10340831232, "io_time": 44083600, "sectors_read": 1836124319, "writes_completed": 7357899, "weighted_io_time": 132609732, "inodes_free": 1192403, "reads_completed": 27584070, "read_time": 298349136, "writes_merged": 1569161, "inodes": 1280000, "device": "/dev/sda1", "sectors_written": 339114072, "reads_merged": 3830089, "has_inodes": true, "usage": 3985969152, "write_time": 10228632, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 51929088, "capacity": 60985344, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 71718, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 74444, "device": "tmpfs", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 9056256, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 5637185536, "capacity": 10340831232, "io_time": 96157472, "sectors_read": 5500795231, "writes_completed": 10807390, "weighted_io_time": 262362688, "inodes_free": 1191724, "reads_completed": 74970732, "read_time": 468791932, "writes_merged": 2447338, "inodes": 1280000, "device": "/dev/sda1", "sectors_written": 510582792, "reads_merged": 10446189, "has_inodes": true, "usage": 4686868480, "write_time": 10072652, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 67108864, "capacity": 67108864, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 74443, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 74444, "device": "shm", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 0, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 7372996608, "capacity": 10340831232, "io_time": 7030452, "sectors_read": 292392161, "writes_completed": 19981660, "weighted_io_time": 24071076, "inodes_free": 1193221, "reads_completed": 3403200, "read_time": 28540088, "writes_merged": 4234349, "inodes": 1280000, "device": "/dev/sda1", "sectors_written": 303279512, "reads_merged": 509925, "has_inodes": true, "usage": 2951057408, "write_time": 11640704, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 67108864, "capacity": 67108864, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 74443, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 74444, "device": "shm", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 0, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}, {"available": 52400128, "capacity": 60985344, "io_time": 0, "sectors_read": 0, "writes_completed": 0, "weighted_io_time": 0, "inodes_free": 71989, "reads_completed": 0, "read_time": 0, "writes_merged": 0, "inodes": 74444, "device": "tmpfs", "sectors_written": 0, "reads_merged": 0, "has_inodes": true, "usage": 8585216, "write_time": 0, "type": "vfs", "io_in_progress": 0, "base_usage": 0}], "task_stats": {"nr_stopped": 0, "nr_sleeping": 0, "nr_uninterruptible": 0, "nr_running": 0, "nr_io_wait": 0}, "diskio": {"io_service_bytes": [{"device": "/dev/sda", "major": 8, "stats": {"Read": 328560128, "Async": 440613425152, "Write": 449184505856, "Total": 449513065984, "Sync": 8899640832}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "/dev/sda", "major": 8, "stats": {"Read": 375639552, "Async": 632165187584, "Write": 645268078592, "Total": 645643718144, "Sync": 13478530560}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}, {"device": "/dev/sda", "major": 8, "stats": {"Read": 417633280, "Async": 146866446336, "Write": 170888749056, "Total": 171306382336, "Sync": 24439936000}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}], "io_serviced": [{"device": "/dev/sda", "major": 8, "stats": {"Read": 17268, "Async": 6519824, "Write": 8609407, "Total": 8626675, "Sync": 2106851}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "/dev/sda", "major": 8, "stats": {"Read": 21887, "Async": 9674169, "Write": 12813376, "Total": 12835263, "Sync": 3161094}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 7}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 6}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 4}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 3}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 1}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 0}, {"device": "/dev/sda", "major": 8, "stats": {"Read": 8707, "Async": 17297911, "Write": 23084989, "Total": 23093696, "Sync": 5795785}, "minor": 0}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 5}, {"device": "", "major": 7, "stats": {"Read": 0, "Async": 0, "Write": 0, "Total": 0, "Sync": 0}, "minor": 2}]}, "memory": {"cache": 50888704, "working_set": 1023115264, "failcnt": 0, "hierarchical_data": {"pgfault": 512213, "pgmajfault": 5917}, "swap": 0, "usage": 1190318080, "rss": 700514304, "container_data": {"pgfault": 512213, "pgmajfault": 5917}, "max_usage": 2352873472}, "cpu": {"usage": {"per_cpu_usage": [86016032804509, 127085001891550, 230915408126829], "total": 444016442822888, "user": 258352170000000, "system": 141379920000000}, "load_average": 0, "cfs": {"throttled_time": 0, "periods": 0, "throttled_periods": 0}}}'
    ]
]

discovery = {
    '': [],
    'fs': [(u'/dev/sda1', {}), (u'shm', {})],
    'network': [(u'cbr0', {}), (u'eth0', {})]
}

checks = {
    'fs': [
        (
            u'/dev/sda1', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '37.63% used (10.87 of 28.89 GB)', [
                        (
                            u'/dev/sda1', 11133.41015625, 23668.284375,
                            26626.819921875, 0, 29585.35546875
                        ), ('fs_size', 29585.35546875, None, None, None, None),
                        (
                            'inodes_used', 262652, 3456000.0, 3648000.0, 0.0,
                            3840000.0
                        )
                    ]
                )
            ]
        ),
        (
            u'shm', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '38.21% used (3.73 of 9.76 GB)', [
                        (
                            u'shm', 3817.31640625, 7991.828125, 8990.806640625,
                            0, 9989.78515625
                        ), ('fs_size', 9989.78515625, None, None, None, None),
                        (
                            'inodes_used', 87599, 1285999.2,
                            1357443.5999999999, 0.0, 1428888.0
                        )
                    ]
                )
            ]
        )
    ],
    'network': [
        (
            u'cbr0', {}, [
                (0, 'In: 0.00 B/s', [('in', 0.0, None, None, None, None)]),
                (0, 'Out: 0.00 B/s', [('out', 0.0, None, None, None, None)]),
                (
                    0, '', [
                        ('if_in_pkts', 0.0, None, None, None, None),
                        ('if_in_errors', 0.0, None, None, None, None)
                    ]
                ), (0, 'Input error rate: 0.00 1/s', []),
                (
                    0, '', [
                        ('if_out_pkts', 0.0, None, None, None, None),
                        ('if_out_errors', 0.0, None, None, None, None)
                    ]
                ), (0, 'Output error rate: 0.00 1/s', []),
                (
                    0, 'Input Discards: 0.00 1/s', [
                        ('if_in_discards', 0.0, None, None, None, None)
                    ]
                ),
                (
                    0, 'Output Discards: 0.00 1/s', [
                        ('if_out_discards', 0.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            u'eth0', {}, [
                (0, 'In: 0.00 B/s', [('in', 0.0, None, None, None, None)]),
                (0, 'Out: 0.00 B/s', [('out', 0.0, None, None, None, None)]),
                (
                    0, '', [
                        ('if_in_pkts', 0.0, None, None, None, None),
                        ('if_in_errors', 0.0, None, None, None, None)
                    ]
                ), (0, 'Input error rate: 0.00 1/s', []),
                (
                    0, '', [
                        ('if_out_pkts', 0.0, None, None, None, None),
                        ('if_out_errors', 0.0, None, None, None, None)
                    ]
                ), (0, 'Output error rate: 0.00 1/s', []),
                (
                    0, 'Input Discards: 0.00 1/s', [
                        ('if_in_discards', 0.0, None, None, None, None)
                    ]
                ),
                (
                    0, 'Output Discards: 0.00 1/s', [
                        ('if_out_discards', 0.0, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}

extra_sections = {'fs': [[]], 'network': [[]]}
