Todo App - Django Project
Layihə Haqqında
Bu layihə sadə bir Todo tətbiqi olaraq hazırlanıb. Tətbiq istifadəçilər üçün öz task-larını izləməyə imkan verir. Hər bir istifadəçi yalnız öz tasklarını görə bilər, amma adminlər bütün istifadəçilərin tasklarını görə bilərlər. Tətbiq həmçinin email vasitəsilə istifadəçini tamamlanmamış tasklar haqqında xəbərdar edir və müəyyən aralıqlarla keçirilmiş taskları silir.

Layihənin Tələbləri
User modelinin özəlləşdirilməsi: Default username əvəzinə email istifadə edərək istifadəçi modeli yaradılmalıdır. username sahəsi silinmişdir.

Todo modelinin yaradılması:

title: Tapşırığın başlığı.
description: Tapşırığın təsviri.
author: Tapşırığı yazan istifadəçi (One-to-many əlaqəsi ilə User modelinə bağlıdır).
due_date: Tapşırığın tamamlanma tarixi.
is_finished: Tapşırığın tamamlanıb-tamamlanmadığını göstərən Boolean dəyər.
API-lar:

İstifadəçi üçün giriş.
Yeni istifadəçi qeydiyyatı.
Parol sıfırlanması.
İstifadəçi məlumatlarının yenilənməsi.
Bütün istifadəçilərin siyahısı (adminlər üçün).
Bir istifadəçinin detalları.
Yeni todo əlavə etmək.
Mövcud todo-nu redaktə etmək.
Todo silmək.
Bütün todoları görmək (adminlər üçün).
Bir todo-nun detalları.
Custom Permissions:

Hər bir istifadəçi yalnız öz todo-larını görə və redaktə edə bilər.
Adminlər bütün istifadəçilərin və todo-ların üzərində əməliyyatlar apara bilərlər.
Docker ilə inteqrasiya:

Layihə dockerize edilmişdir və Dockerfile və docker-compose vasitəsilə işə salma zamanı requirements.txt oxunmasında problem var . Həmin fayl open olmur .
Celery ilə Periodic Tasks:

Həftəlik silinmə: Keçmiş tamamlanmamış todo-lar hər həftə silinir.
Həftəlik xəbərdarlıq: Vaxtı keçmiş tapşırıqların müəlliflərinə email ilə "todo-nuzu etməmisiniz" mesajı göndərilir.
