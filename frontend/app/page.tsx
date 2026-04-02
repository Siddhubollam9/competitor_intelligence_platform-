"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [analysis, setAnalysis] = useState<any>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/analysis/")
      .then((res) => res.json())
      .then((data) => setAnalysis(data))
      .catch((err) => console.error(err));
  }, []);

  if (!analysis) {
    return <div className="p-10 text-xl">Loading...</div>;
  }

  const insights = analysis.insights || {};
  const rec = {
  messaging: analysis.recommendations?.messaging || [],
  channels: analysis.recommendations?.channels || [],
  gtm_strategy: analysis.recommendations || []
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-4xl font-bold mb-10 text-black">
        🚀 AI Competitive Intelligence Dashboard
      </h1>

      {/* INSIGHTS */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        <Card title="📊 Features" data={insights.features || []} />
        <Card title="📣 Messaging Trends" data={insights.messaging_trends || []} />
        <Card title="😡 Customer Pain Points" data={insights.customer_pain_points || []} />
        <Card title="⚠️ Weaknesses" data={insights.weaknesses || []} />

      </div>

      {/* RECOMMENDATIONS */}
      <div className="mt-10 bg-white p-6 rounded-xl shadow">
        <h2 className="text-2xl font-bold mb-6 text-black">
          💡 Strategy Recommendations
        </h2>

        <Section title="Messaging Strategy" data={rec.messaging || []} />
        <Section title="Channels" data={rec.channels || []} />

        {/* GTM STRATEGY */}
        <div className="mt-6">
          <h3 className="text-xl font-semibold mb-3 text-black">
            🚀 GTM Strategy
          </h3>

          {Array.isArray(rec.gtm_strategy) && rec.gtm_strategy.length > 0 ? (
            rec.gtm_strategy.map((phase: any, index: number) => (
              <div key={index} className="mb-5 border p-4 rounded-lg bg-gray-50">

                {/* Structured case */}
                {phase.phase ? (
                  <>
                    <h4 className="font-bold text-lg text-black">
                      {phase.phase}
                    </h4>
                    <p className="text-gray-700 mb-2">{phase.goal}</p>

                    <ul className="list-disc pl-5 text-gray-800">
                      {phase.tactics?.map((t: string, i: number) => (
                        <li key={i}>{t}</li>
                      ))}
                    </ul>
                  </>
                ) : (
                  /* Fallback case */
                  <p className="text-gray-800">{phase}</p>
                )}

              </div>
            ))
          ) : (
            <p className="text-gray-500">No GTM strategy available</p>
          )}
        </div>
      </div>
    </div>
  );
}

/* CARD COMPONENT */
function Card({ title, data }: any) {
  return (
    <div className="bg-white p-5 rounded-xl shadow">
      <h2 className="text-xl font-semibold mb-3 text-black">{title}</h2>
      <ul className="list-disc pl-5 text-gray-800">
        {data.map((item: string, index: number) => (
          <li key={index} className="mb-1">{item}</li>
        ))}
      </ul>
    </div>
  );
}

/* SECTION COMPONENT */
function Section({ title, data }: any) {
  return (
    <div className="mb-6">
      <h3 className="text-xl font-semibold mb-3 text-black">{title}</h3>
      <ul className="list-disc pl-5 text-gray-800">
        {data.map((item: string, index: number) => (
          <li key={index} className="mb-1">{item}</li>
        ))}
      </ul>
    </div>
  );
}