
def generate_output_by_vulns(db_cursor, db_connection, outputfile):
    for vulnerability in ['sslv3', 'sslv2', 'CRIME', 'heartbleed', 'reneg', 'weakmediumcipher', 'rc4']:
        outputfile.write("\n+++++"+vulnerability+"+++++\n----------------------------------------\n")
        #db_cursor.execute('''SELECT ip, hostname, port FROM hosts WHERE (?)=1''', (vulnerability,))
        db_cursor.execute("SELECT ip, hostname, port FROM hosts WHERE "+vulnerability+"=1")#, (vulnerability,))
        liste = db_cursor.fetchall()
        for i in liste:
            out_str = i[0] + ":" + i[2] + " (" + i[1] + ")\n"
            outputfile.write(out_str)
        outputfile.write("\n")
    # certificate
    outputfile.write("\n+++++certificate+++++\n----------------------------------------\n")
    db_cursor.execute("SELECT ip, hostname, port, certificate FROM hosts WHERE certificate IS NOT ''")
    liste = db_cursor.fetchall()
    for j in liste:
        out_str = j[0] + ":" + j[2] + " (" + j[1] + ") - " + j[3] + "\n"
        outputfile.write(out_str)
    outputfile.write("\n")
    # info output
    outputfile.write("\n+++++info+++++\n----------------------------------------\n")
    db_cursor.execute("SELECT ip, hostname, port, info FROM hosts WHERE info IS NOT ''")
    liste = db_cursor.fetchall()
    for k in liste:
        out_str = k[0] + ":" + k[2] + " (" + k[1] + ") - " + k[3] + "\n"
        outputfile.write(out_str)
    outputfile.write("\n")

def attach_invalidtargets_to_output(db_cursor, db_connection, outputfile):
    outputfile.write("\n\n\nInvalid targets:\n----------------------------------------\n")
    db_cursor.execute("SELECT name FROM invalidtargets")
    liste = db_cursor.fetchall()
    for i in liste:
        out_str = str(i[0]) + "\n"
        outputfile.write(out_str)
    outputfile.write("\n")