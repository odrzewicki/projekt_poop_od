from tkinter import *
import tkintermapview
from models import Parking, Worker, User
from data.init_data import parkings_data, workers_data, users_data

# ====================== LISTY ======================
parkings = []
workers = []
users = []

# ====================== GUI ======================
root = Tk()
root.title("System Parkingowy")
root.geometry("1300x900")

frame_top = Frame(root)
frame_top.pack(pady=10)

frame_parking = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_parking.grid(row=0, column=0, padx=10)

frame_worker = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_worker.grid(row=0, column=1, padx=10)

frame_user = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_user.grid(row=0, column=2, padx=10)

frame_maps = Frame(root)
frame_maps.pack(pady=20)

# Mapy
Label(frame_maps, text="Mapa parkingów").grid(row=0, column=0)
Label(frame_maps, text="Mapa pracowników").grid(row=0, column=1)
Label(frame_maps, text="Mapa użytkowników").grid(row=0, column=2)

map_parking = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_parking.grid(row=1, column=0, padx=5)
map_parking.set_position(52.23, 21.01)
map_parking.set_zoom(6)

map_worker = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_worker.grid(row=1, column=1, padx=5)
map_worker.set_position(52.23, 21.01)
map_worker.set_zoom(6)

map_user = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_user.grid(row=1, column=2, padx=5)
map_user.set_position(52.23, 21.01)
map_user.set_zoom(6)

# Dane z plików
for item in parkings_data:
    p = Parking(item["parking_name"], item["parking_location"], map_parking)
    parkings.append(p)

for item in workers_data:
    w = Worker(item["worker_name"], item["worker_parking"], item["worker_location"], map_worker)
    workers.append(w)

for item in users_data:
    u = User(item["user_name"], item["user_parking"], item["user_location"], map_user)
    users.append(u)

root.mainloop()
