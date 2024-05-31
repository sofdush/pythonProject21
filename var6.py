import streamlit as st
import matplotlib.pyplot as plt

def get_var6(lines, selected_port):
    ports = {'C': 'Шербур', 'Q': 'Квинстаун', 'S': 'Саутгемптон'}
    result = {'survived': [], 'perished': []}

    for line in lines:
        data = line.strip().split(',')
        if data[1].isdigit():
            survived = int(data[1])
            fare = float(data[10]) if data[10] else 0.0
            port = data[12]
            if port == selected_port:
                if survived == 1:
                    result['survived'].append(fare)
                else:
                    result['perished'].append(fare)

    avg_survived = sum(result['survived']) / len(result['survived']) if result['survived'] else 0
    avg_perished = sum(result['perished']) / len(result['perished']) if result['perished'] else 0

    return avg_survived, avg_perished

def main():
    st.title('Средняя стоимость билета у спасенных и погибших пассажиров')

    ports = {'C': 'Шербур', 'Q': 'Квинстаун', 'S': 'Саутгемптон'}
    port_keys = list(ports.keys())
    port_values = list(ports.values())

    selected_port_value = st.selectbox("Выберите порт посадки", port_values)
    selected_port = port_keys[port_values.index(selected_port_value)]

    with open("data.csv") as file:
        lines = file.readlines()

    avg_survived, avg_perished = get_var6(lines, selected_port)

    st.write(f"Средняя стоимость билета для спасенных пассажиров в порту {selected_port_value}: {avg_survived}")
    st.write(f"Средняя стоимость билета для погибших пассажиров в порту {selected_port_value}: {avg_perished}")

    fig=plt.figure(figsize=(10,5))
    plt.bar(['Спасенные', 'Погибшие'], [avg_survived, avg_perished], color=['green', 'red'])
    plt.xlabel('Статус')
    plt.ylabel('Средняя цена')
    plt.suptitle(f'Средняя стоимость билета в порту {selected_port_value}')
    st.pyplot(fig)

main()