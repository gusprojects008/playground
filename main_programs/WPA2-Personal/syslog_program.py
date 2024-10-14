import syslog

def log_Program(program):
    try:
       syslog.openlog(program) # OPEN CONNECTION WITH syslog.
       syslog.syslog(syslog.LOG_INFO, "This is a log Info")
       syslog.syslog(syslog.LOG_WARNING, "This is a log alert")
       syslog.syslog(syslog.LOG_ERR, "This is a log erro")
    except Exception as error:
           syslog.syslog(syslog.LOG_ERR, f"Logging error: {error}")
    finally:
           syslog.closelog()

program_user = input("Type it the name program for Log: ")

if __name__ == "__main__":
   log_Program(program_user)
