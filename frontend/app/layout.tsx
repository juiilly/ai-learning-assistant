import "./globals.css";

export const metadata = {
  title: "AI Learning Assistant",
  description: "AI powered learning app",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        style={{
          margin: 0,
          fontFamily: "system-ui, sans-serif",
          backgroundColor: "#f3f4f6",
        }}
      >
        {children}
      </body>
    </html>
  );
}