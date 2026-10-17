//! Windows only: embed the app icon and version info (VERSIONINFO) into `photosweet.exe`.
//!
//! On every other target this does nothing. A missing resource compiler is a warning, so a
//! cross-compile from macOS or Linux still links, unless `PHOTOSWEET_REQUIRE_WINRES=1` (set by the
//! release workflow) turns it into an error.

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-changed=../../assets/app-icon/photosweet.ico");
    println!("cargo:rerun-if-env-changed=PHOTOSWEET_REQUIRE_WINRES");
    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() != Ok("windows") {
        return;
    }
    let mut res = winresource::WindowsResource::new();
    res.set_icon("../../assets/app-icon/photosweet.ico")
        .set("ProductName", "PhotoSweet")
        .set("FileDescription", "PhotoSweet image editor")
        .set("CompanyName", "salim-slimani")
        .set("LegalCopyright", "Copyright (c) 2026 salim-slimani. MIT OR Apache-2.0.")
        .set("OriginalFilename", "photosweet.exe")
        .set("InternalName", "photosweet");
    if let Err(e) = res.compile() {
        if std::env::var_os("PHOTOSWEET_REQUIRE_WINRES").is_some() {
            panic!("embedding Windows resources failed: {e}");
        }
        println!("cargo:warning=photosweet.exe built without icon/version resources: {e}");
    }
}
