from fastapi import APIRouter, HTTPException
from conn import create_conn

router = APIRouter()

@router.post("/absensi")
async def absensi():
    conn = create_conn()
    cur = conn.cursor()
    cur.execute("SELECT * from absensi")
    # The method used when you want to display everything is fetchall and to display just one it is fetchone
    result = cur.fetchall()
    cur.close()
    conn.close()
    try: 
        data = [{"Nama": row[0], "Keterangan": row[1], "Tanggal": row[2], "Nilai": row[3], "Info": row[4]} for row in result]
    except ZeroDivisionError as e:
        return HTTPException(status_code=400, detail=str(e))
    return {
        "status": 200,
        "message": "OK",
        "daily_trend": data
    }