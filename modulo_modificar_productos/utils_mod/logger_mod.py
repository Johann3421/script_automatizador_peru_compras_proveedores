"""
logger_mod.py — Logger thread-safe para el módulo de modificación de productos.
Igual al logger del proyecto principal pero independiente para no generar dependencias.
"""
import queue
import threading


class LogWriter:
    """Escribe mensajes en una queue thread-safe."""

    def __init__(self, q: queue.Queue):
        self._q = q
        self._lock = threading.Lock()

    def _put(self, level: str, msg: str):
        with self._lock:
            self._q.put((level, msg))

    def info(self, msg: str):
        self._put("INFO", msg)

    def ok(self, msg: str):
        self._put("OK", msg)

    def warn(self, msg: str):
        self._put("WARN", msg)

    def error(self, msg: str):
        self._put("ERROR", msg)

    def done(self, ok: int, err: int):
        self._put("DONE", f"Completado: {ok} OK, {err} errores")
