export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, phone, email, date, guests, message } = req.body;

  if (!name || !phone) {
    return res.status(400).json({ error: 'Jméno a telefon jsou povinné.' });
  }

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    return res.status(500).json({ error: 'Server není nakonfigurován.' });
  }

  const dateFormatted = date
    ? new Date(date).toLocaleDateString('cs-CZ', { day: 'numeric', month: 'long', year: 'numeric' })
    : '—';

  const emailHtml = `
    <h2 style="font-family:serif;color:#1E293B;">Nová poptávka ze stránky U Cerhů</h2>
    <table style="border-collapse:collapse;width:100%;font-family:sans-serif;font-size:14px;color:#1E293B;">
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;width:140px;">Jméno</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${name}</td></tr>
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;">Telefon</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${phone}</td></tr>
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;">E-mail</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${email || '—'}</td></tr>
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;">Termín</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${dateFormatted}</td></tr>
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;">Počet hostů</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${guests || '—'}</td></tr>
      <tr><td style="padding:8px 12px;background:#f8f6f1;font-weight:600;vertical-align:top;">Zpráva</td><td style="padding:8px 12px;">${message ? message.replace(/\n/g, '<br>') : '—'}</td></tr>
    </table>
    <p style="font-family:sans-serif;font-size:12px;color:#9ca3af;margin-top:24px;">Odesláno přes kontaktní formulář na ucerhu.cz</p>
  `;

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'Web U Cerhů <onboarding@resend.dev>',
        to: ['jiri_barton@centrum.cz'],
        reply_to: email || undefined,
        subject: `Nová poptávka: ${name}${date ? ` — ${dateFormatted}` : ''}`,
        html: emailHtml,
      }),
    });

    if (!response.ok) {
      const err = await response.json();
      console.error('Resend error:', err);
      return res.status(500).json({ error: 'Nepodařilo se odeslat e-mail.' });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Contact handler error:', err);
    return res.status(500).json({ error: 'Chyba serveru.' });
  }
}
