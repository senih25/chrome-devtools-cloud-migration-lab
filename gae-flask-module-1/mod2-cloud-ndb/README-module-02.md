# Module 02 — App Engine NDB to Cloud NDB Migration

## Amaç

Bu modülde App Engine NDB yaklaşımından google-cloud-ndb istemci kütüphanesine geçiş pratiği yapıldı.

## Yapılanlar

- Modül 2 çalışma klasörü oluşturuldu: mod2-cloud-ndb
- app.yaml Python 3.12 App Engine Standard yapısına güncellendi.
- requirements.txt modern Python 3 uyumlu hale getirildi.
- google-cloud-ndb kullanımı doğrulandı.
- Datastore composite index hatası analiz edildi.
- index.yaml ile gerekli index yüklendi.
- Index READY durumuna geldikten sonra local test başarılı oldu.
- App Engine deploy başarılı oldu.
- Chrome DevTools ile canlı doğrulama yapıldı.

## Karşılaşılan Hata

İlk hata:

    google.api_core.exceptions.FailedPrecondition:
    400 no matching index found

Sonraki durum:

    The index for this query is not ready to serve

Çözüm:

    gcloud datastore indexes create index.yaml
    gcloud datastore indexes list

## Deploy Bilgisi

Project: trustable-ai-100mph
Service: default
URL: https://trustable-ai-100mph.ew.r.appspot.com
Runtime: python312

## DevTools Doğrulama

Network: GET /?guestbook_name= → 200
Console: Kritik hata yok
Local Storage: boş
Session Storage: boş
Cookies: boş
Cache Storage: boş

## Güvenlik Notu

Bu modülde yalnızca demo guestbook verisi kullanıldı. Gerçek sağlık verisi, PHI, e-Nabız exportu veya kişisel veri kullanılmadı.

## Portföy Kazanımı

Cloud NDB migration sonrası Datastore composite index hatasını analiz ettim; index.yaml ile gerekli index’i oluşturup App Engine üzerinde canlı doğrulama yaptım. Chrome DevTools Network, Console ve Application panelleriyle deploy sonrası davranışı doğruladım.

## CV Cümlesi

Migrated an App Engine sample from legacy NDB concepts to Cloud NDB, configured Python 3.12 App Engine Standard deployment, resolved Datastore composite index requirements, and validated the live application using Chrome DevTools Network, Console, and Application panels.

## Safe Reuse for Related Repositories

1. Allowed public-safe documentation/checklist pattern:
   - Cloud NDB migration notes
   - Datastore composite index troubleshooting checklist
   - DevTools Network/Console/Application verification pattern
   - Python 3.12 App Engine deployment checklist

2. Needs manual review:
   - adapting the index/debugging checklist to sensitive local dashboards
   - using the checklist for PHI-free aggregate export consumers

3. Forbidden sensitive-data coupling:
   - raw health data transfer
   - e-Nabız export use
   - patient-level processing
   - direct runtime integration with sensitive health repositories

## Evidence Pointers

- Python 3.12 App Engine Standard configuration was used.
- `gunicorn` entrypoint was configured.
- `google-cloud-ndb` usage was verified.
- Datastore composite index requirement was identified and resolved.
- Index reached `READY` state before final verification.
- Chrome DevTools verification covered Network, Console, and Application checks.
- Full live endpoint is intentionally omitted from top-level public-facing docs.
