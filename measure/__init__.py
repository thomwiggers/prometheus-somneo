#!/usr/bin/env python3

import sys
import os
import time

from prometheus_client import CollectorRegistry, Gauge, start_http_server

from pysomneo import Somneo


def run():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <somneo host>")
        sys.exit(1)

    start_http_server(int(os.environ.get("LISTEN_PORT", 9101)))

    somneo = Somneo(host)
    somneo.update()
    temperature = Gauge('somneo_temperature', 'Temperature in degrees celcius')
    humidity = Gauge('somneo_humidity', 'Humidity')
    luminance = Gauge('somneo_luminance', 'Luminance')
    noise = Gauge('somneo_noise', 'Noise level')


    while True:
        somneo.update()
        temperature.set(somneo.temperature())
        humidity.set(somneo.humidity())
        luminance.set(somneo.luminance())
        noise.set(somneo.noise())

        time.sleep(30)


if __name__ == "__main__":
    run()
