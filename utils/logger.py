import queue


class LogWriter:
    def __init__(self, log_queue: queue.Queue):
        self._q = log_queue

    def info(self, msg: str):
        self._q.put({"type": "log", "level": "info", "msg": msg})

    def ok(self, msg: str):
        self._q.put({"type": "log", "level": "ok", "msg": msg})

    def error(self, msg: str):
        self._q.put({"type": "log", "level": "error", "msg": msg})

    def warn(self, msg: str):
        self._q.put({"type": "log", "level": "warn", "msg": msg})

    def progress(self, current: int, total: int):
        self._q.put({"type": "progress", "current": current, "total": total})

    def done(self, ok_count: int, error_count: int):
        self._q.put({"type": "done", "ok": ok_count, "errors": error_count})
