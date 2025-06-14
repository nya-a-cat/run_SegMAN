from analyze_logs import load_json_logs, plot_curve
from argparse import Namespace
import json

if __name__ == '__main__':
    demo_log = 'demo_log.json'
    with open(demo_log, 'w') as f:
        json.dump({'epoch': 1, 'mIoU': 0.6, 'mode': 'train', 'iter': 1}, f)
        f.write('\n')
        json.dump({'epoch': 2, 'mIoU': 0.65, 'mode': 'train', 'iter': 2}, f)
        f.write('\n')
    args = Namespace(
        json_logs=[demo_log],
        keys=['mIoU'],
        legend=None,
        title='Demo mIoU Curve',
        backend='agg',
        style='dark',
        out='demo_curve.png'
    )
    log_dicts = load_json_logs(args.json_logs)
    plot_curve(log_dicts, args)
    print('Saved demo_curve.png')
