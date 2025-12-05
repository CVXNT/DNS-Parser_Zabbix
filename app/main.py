#!/usr/bin/env python3

# DNS Parser - парсинг всех типов DNS записей для домена
# Использование: python main.py <domain>
# Вывод: каждая строка содержит только значение DNS записи


import sys
import dns.resolver
import dns.exception


def parse_dns(domain):
    # Парсит все типы DNS записей для указанного домена
    
    # Args:
    #     domain: доменное имя для парсинга

    # Типы DNS записей для проверки в строгом порядке
    record_types = ['A', 'MX', 'NS', 'TXT']
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            # Собираем все значения для сортировки
            values = []
            
            for rdata in answers:
                # Форматируем значение без типа записи
                if record_type == 'MX':
                    # Для MX записей убираем приоритет и выводим только сервер
                    values.append(str(rdata.exchange).rstrip('.'))
                elif record_type == 'TXT':
                    # Для TXT записей убираем кавычки
                    values.append(str(rdata).strip('"'))
                elif record_type == 'SOA':
                    # Для SOA выводим основной nameserver
                    values.append(str(rdata.mname).rstrip('.'))
                else:
                    # Для остальных записей выводим как есть, убирая точку в конце
                    values.append(str(rdata).rstrip('.'))
            
            # Сортируем значения для детерминированного вывода
            values.sort()
            
            # Выводим отсортированные значения
            for value in values:
                print(value)
                
        except dns.resolver.NoAnswer:
            # Нет записей этого типа - пропускаем
            pass
        except dns.resolver.NXDOMAIN:
            # Домен не существует
            print(f"Error: Domain {domain} does not exist", file=sys.stderr)
            sys.exit(1)
        except dns.exception.Timeout:
            # Таймаут при запросе
            pass
        except Exception:
            # Другие ошибки - пропускаем
            pass


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <domain>", file=sys.stderr)
        sys.exit(1)
    
    domain = sys.argv[1]
    parse_dns(domain)


if __name__ == "__main__":
    main()
