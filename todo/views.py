from django.shortcuts import HttpResponse


def task_list(request):
    html_response = """

            <h1>Yangi vazifa yaratish</h1>
<form>

    <label for="name">Vazifa nomi:
    <input type="text" name="name" id="name">
    </label>

    <br><br>
    <label for="tavsif">Tavsif: 
    <textarea name="textarea" id="tavsif"></textarea>
    </label>

    <br><br>
    <label for="muddat">Muddat: 
    <input type="date" name="muddat" id="muddat">
    </label>

    <br><br>
    <label for="degree"> Muhimlik darajasi: 
        <select name="degree" id="degree">
            <option value="past">Past</option>
            <option value="orta">O'rta</option>
            <option value="yuqori">Yuqori</option>
        </select>
    </label>

    <br><br>
    <button>Vazifani saqlash</button>

</form>

<h1>Mavjud vazifalar</h1>
<table>
    <thead>
        <tr>
            <th>Vazifa</th>
            <th>Tavsif</th>
            <th>Muhimlik</th>
            <th>Muddat</th>
            <th>Holat</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>oylik moliyaviy hisobotni va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>oylik moliyaviy hisobotni va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>oylik moliyaviy hisobotni va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>oylik moliyaviy hisobotni va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>oylik moliyaviy hisobotni va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
    </tbody>


</table>

        """
    return HttpResponse(html_response)
