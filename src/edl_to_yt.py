from datetime import timedelta
from pathlib import Path
from collections import OrderedDict


def read_edl(path: Path) -> list[str]:
    if path is None:
        return []
    elif not path.exists():
        raise FileNotFoundError('path has no destination')
    elif not path.is_file():
        raise ValueError('path is not a regular file')
    elif not str(path).split('.')[-1].endswith('edl'):
        raise ValueError('file is not .edl')

    with open(file=path, mode='r', encoding='utf-8') as edl:
        return edl.readlines()


def parse_input(
        input_lines: list[str],
        start_timestamp: timedelta = timedelta(hours=1),
        ignore_errors=False
) -> OrderedDict[timedelta, str]:
    d: OrderedDict[timedelta, str] = OrderedDict()

    for i in range(3, len(input_lines), 3):
        if input_lines[i] == '\n':
            break

        h, m, s = map(int, input_lines[i].strip(' \n').split(' ')[-4].split(':')[:-1])

        timestamp_delta = timedelta(hours=h, minutes=m, seconds=s) - start_timestamp

        if i == 3 and timestamp_delta != timedelta(milliseconds=0):
            if ignore_errors:
                continue
            raise ValueError('first timestamp must be 0:00')
        if d and timestamp_delta - next(reversed(d)) < timedelta(seconds=10):
            if ignore_errors:
                continue
            raise ValueError(f'timestamps must be at least 10 seconds apart (marker {len(d) + 1})')

        description = input_lines[i + 1].split(' |M:')[1].split(' |D:1\n')[0]

        d[timestamp_delta] = description

    return d


def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f'{hours:01}:{minutes:02}:{seconds:02}' if hours < 10 else f'{hours:02}:{minutes:02}:{seconds:02}'
    else:
        return f'{minutes:01}:{seconds:02}' if minutes < 10 else f'{minutes:02}:{seconds:02}'


def output_to_file(d: OrderedDict, path: Path = 'timestamps.txt') -> None:
    with open(path, 'w', encoding='utf-8') as txt:
        txt.write(string_value(d))


def string_value(d: OrderedDict) -> str:
    return '\n'.join([f'{format_timedelta(k)} {v}' for k, v in d.items()])


def string_from_path(path: Path) -> str:
    lines: list[str] = read_edl(path)
    entries: OrderedDict[timedelta, str] = parse_input(lines)
    return string_value(entries)


def print_ordered_dict(d: OrderedDict) -> None:
    if not isinstance(d, OrderedDict):
        raise TypeError('The provided argument is not an OrderedDict.')

    for key, value in d.items():
        print(f'{key}: {value}')


def main() -> None:
    input_path: Path = Path(input('Enter path to .edl file > '))
    output_path: Path = Path(input('Enter output path > '))

    lines: list[str] = read_edl(input_path)

    entries: OrderedDict[timedelta, str] = parse_input(lines)

    output_to_file(entries, output_path)
    print('SUCCESS')


if __name__ == '__main__':
    main()
